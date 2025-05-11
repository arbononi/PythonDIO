from typing import Type, TypeVar, Generic, List, Optional, Tuple
from dataclasses import fields, is_dataclass
from datetime import date, datetime

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, banco, model_cls: Type[T], table: str):
        if not is_dataclass(model_cls):
            raise TypeError("Modelo dever ser do tipo @dataclass")
        self.banco = banco
        self.model = model_cls
        self.table = table

    def add(self, obj: T) -> Tuple[bool, int, str]:
        cols = [f.name for f in fields(obj) if f.name != "id"]
        ph = ",".join("?" for _ in cols)
        sql = f"INSERT INTO {self.table} ({','.join(cols)}) VALUES ({ph})"
        vals = self._to_tuple(obj, exclude_id=True)
        cur, err = self.banco.executar(sql, vals)
        return (True, cur.lastrowid, "") if cur else (False, 0, err)

    def update(self, obj: T) -> Tuple[bool, str]:
        if self.table == "versoes":
            cols = [f.name for f in fields(obj) if f.name != "versao"]
        else:
            cols = [f.name for f in fields(obj) if f.name != "id"]
        assigns = ",".join(f"{c}=?" for c in cols)
        if self.table == "versoes":
            sql = f"UPDATE {self.table} SET {assigns} WHERE versao=?"
            vals = self._to_tuple(obj, exclude_id=True) + (obj.versao,)
        else:
            sql = f"UPDATE {self.table} SET {assigns} WHERE id=?"
            vals = self._to_tuple(obj, exclude_id=True) + (obj.id,)
        cur, err = self.banco.executar(sql, vals)
        return (True, "") if cur else (False, err)

    def delete_by_id(self, id: int) -> Tuple[bool, str]:
        if self.table == "versoes":
            sql = f"DELETE FROM {self.table} WHERE versao=?"
        else:
            sql = f"DELETE FROM {self.table} WHERE id=?"
        cur, err = self.banco.executar(sql, (id,))
        return (True, "") if cur else (False, err)

    def get_by_id(self, id: int) -> Tuple[Optional[T], str]:
        if self.table == "versoes":
            sql = f"SELECT * FROM {self.table} WHERE versao=?"
        else:
            sql = f"SELECT * FROM {self.table} WHERE id=?"
        cur, err = self.banco.executar(sql, (id,))
        if cur:
            row = cur.fetchone()
            return (self._from_row(row), "") if row else (None, "")
        return None, err

    def get_all(self, ) -> Tuple[List[T], str]:
        sql = f"SELECT * FROM {self.table}"
        cur, err = self.banco.executar(sql)
        if cur:
            return ([self._from_row(r) for r in cur.fetchall()], "")
        return [], err

    def _to_tuple(self, obj, exclude_id=False):
        out = []
        for f in fields(obj):
            if exclude_id:
               if (self.table == "versoes" and f.name == "versao") or f.name== "id": 
                  continue
            v = getattr(obj, f.name)
            if hasattr(v, "value"): v = v.value
            if isinstance(v, date): v = v.isoformat()
            out.append(v)
        return tuple(out)

    def _from_row(self, row):
        kwargs = {}
        for f in fields(self.model):
            v = row[f.name]
            if hasattr(f.type, "__members__"):
                v = f.type(v)
            elif f.type.__name__=="date" and v:
                v = date.fromisoformat(v)
            elif f.type.__name__=="datetime" and v:
                v = datetime.fromisoformat(v)
            kwargs[f.name] = v
        return self.model(**kwargs)
