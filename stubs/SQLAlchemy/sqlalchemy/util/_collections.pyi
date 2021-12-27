import collections.abc
import sys
from _typeshed import Self, SupportsKeysAndGetItem
from collections.abc import Callable, Iterable, Iterator
from typing import Any, Generic, NoReturn, TypeVar, overload

from ..cimmutabledict import immutabledict as immutabledict
from ..sql.elements import ColumnElement

_S = TypeVar("_S")
_T = TypeVar("_T")

collections_abc = collections.abc

EMPTY_SET: frozenset[Any]

class ImmutableContainer:
    def __delitem__(self, *arg: object, **kw: object) -> NoReturn: ...
    def __setitem__(self, *arg: object, **kw: object) -> NoReturn: ...
    def __setattr__(self, *arg: object, **kw: object) -> NoReturn: ...

def coerce_to_immutabledict(d) -> immutabledict: ...

EMPTY_DICT: immutabledict

class FacadeDict(ImmutableContainer, dict[Any, Any]):
    clear: Any
    pop: Any
    popitem: Any
    setdefault: Any
    update: Any
    def __new__(cls, *args): ...
    def copy(self) -> None: ...  # type: ignore[override]
    def __reduce__(self): ...

class Properties(Generic[_T]):
    def __init__(self, data: dict[str, _T]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __dir__(self) -> list[str]: ...
    def __add__(self, other: Iterable[_S]) -> list[_S | _T]: ...
    def __setitem__(self, key: str, obj: _T) -> None: ...
    def __getitem__(self, key: str) -> _T: ...
    def __delitem__(self, key: str) -> None: ...
    def __setattr__(self, key: str, obj: _T) -> None: ...
    def __getattr__(self, key: str) -> _T: ...
    def __contains__(self, key: str) -> bool: ...
    def as_immutable(self) -> ImmutableProperties[_T]: ...
    def update(self, value: Iterable[tuple[str, _T]] | SupportsKeysAndGetItem[str, _T]) -> None: ...
    @overload
    def get(self, key: str) -> _T | None: ...
    @overload
    def get(self, key: str, default: _S) -> _T | _S: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[_T]: ...
    def items(self) -> list[tuple[str, _T]]: ...
    def has_key(self, key: str) -> bool: ...
    def clear(self) -> None: ...

class OrderedProperties(Properties[_T], Generic[_T]):
    def __init__(self) -> None: ...

class ImmutableProperties(ImmutableContainer, Properties[_T], Generic[_T]): ...

if sys.version_info >= (3, 7):
    OrderedDict = dict
else:
    class OrderedDict(dict[Any, Any]):
        def __reduce__(self): ...
        def __init__(self, ____sequence: Any | None = ..., **kwargs) -> None: ...
        def clear(self) -> None: ...
        def copy(self): ...
        def __copy__(self): ...
        def update(self, ____sequence: Any | None = ..., **kwargs) -> None: ...
        def setdefault(self, key, value): ...
        def __iter__(self): ...
        def keys(self): ...
        def values(self): ...
        def items(self): ...
        def __setitem__(self, key, obj) -> None: ...
        def __delitem__(self, key) -> None: ...
        def pop(self, key, *default): ...
        def popitem(self): ...

def sort_dictionary(d, key: Any | None = ...): ...

class OrderedSet(set[_T], Generic[_T]):
    def __init__(self, d: Iterable[_T] | None = ...) -> None: ...
    def add(self, element: _T) -> None: ...
    def remove(self, element: _T) -> None: ...
    def insert(self, pos: int, element: _T) -> None: ...
    def discard(self, element: _T) -> None: ...
    def clear(self) -> None: ...
    def __getitem__(self, key: int) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __add__(self, other: Iterable[_S]) -> OrderedSet[_S | _T]: ...
    def update(self: Self, iterable: Iterable[_T]) -> Self: ...  # type: ignore[override]
    __ior__ = update  # type: ignore[assignment]
    def union(self, other: Iterable[_S]) -> OrderedSet[_S | _T]: ...  # type: ignore[override]
    __or__ = union  # type: ignore[assignment]
    def intersection(self: Self, other: Iterable[Any]) -> Self: ...  # type: ignore[override]
    __and__ = intersection  # type: ignore[assignment]
    def symmetric_difference(self, other: Iterable[_S]) -> OrderedSet[_S | _T]: ...
    __xor__ = symmetric_difference  # type: ignore[assignment]
    def difference(self: Self, other: Iterable[Any]) -> Self: ...  # type: ignore[override]
    __sub__ = difference  # type: ignore[assignment]
    def intersection_update(self: Self, other: Iterable[Any]) -> Self: ...  # type: ignore[override]
    __iand__ = intersection_update  # type: ignore[assignment]
    def symmetric_difference_update(self: Self, other: Iterable[_T]) -> Self: ...  # type: ignore[override]
    __ixor__ = symmetric_difference_update  # type: ignore[assignment]
    def difference_update(self: Self, other: Iterable[Any]) -> Self: ...  # type: ignore[override]
    __isub__ = difference_update  # type: ignore[assignment]

class IdentitySet:
    def __init__(self, iterable: Any | None = ...) -> None: ...
    def add(self, value) -> None: ...
    def __contains__(self, value): ...
    def remove(self, value) -> None: ...
    def discard(self, value) -> None: ...
    def pop(self): ...
    def clear(self) -> None: ...
    def __cmp__(self, other) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def issubset(self, iterable): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def issuperset(self, iterable): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def union(self, iterable): ...
    def __or__(self, other): ...
    def update(self, iterable) -> None: ...
    def __ior__(self, other): ...
    def difference(self, iterable): ...
    def __sub__(self, other): ...
    def difference_update(self, iterable) -> None: ...
    def __isub__(self, other): ...
    def intersection(self, iterable): ...
    def __and__(self, other): ...
    def intersection_update(self, iterable) -> None: ...
    def __iand__(self, other): ...
    def symmetric_difference(self, iterable): ...
    def __xor__(self, other): ...
    def symmetric_difference_update(self, iterable) -> None: ...
    def __ixor__(self, other): ...
    def copy(self): ...
    __copy__: Any
    def __len__(self): ...
    def __iter__(self): ...
    def __hash__(self): ...

class WeakSequence:
    def __init__(self, __elements=...) -> None: ...
    def append(self, item) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable: Any | None = ...) -> None: ...

class PopulateDict(dict[Any, Any]):
    creator: Any
    def __init__(self, creator) -> None: ...
    def __missing__(self, key): ...

class WeakPopulateDict(dict[Any, Any]):
    creator: Any
    weakself: Any
    def __init__(self, creator_method) -> None: ...
    def __missing__(self, key): ...

column_set = set
column_dict = dict
ordered_column_set = OrderedSet[ColumnElement]

def unique_list(seq: Iterable[_T], hashfunc: Callable[[_T], Any] | None = ...) -> list[_T]: ...

class UniqueAppender:
    data: Any
    def __init__(self, data, via: Any | None = ...) -> None: ...
    def append(self, item) -> None: ...
    def __iter__(self): ...

def coerce_generator_arg(arg): ...
def to_list(x, default: Any | None = ...): ...
def has_intersection(set_, iterable): ...
def to_set(x): ...
def to_column_set(x): ...
def update_copy(d, _new: Any | None = ..., **kw): ...
def flatten_iterator(x) -> None: ...

class LRUCache(dict[Any, Any]):
    capacity: Any
    threshold: Any
    size_alert: Any
    def __init__(self, capacity: int = ..., threshold: float = ..., size_alert: Any | None = ...) -> None: ...
    def get(self, key, default: Any | None = ...): ...
    def __getitem__(self, key): ...
    def values(self): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value) -> None: ...
    @property
    def size_threshold(self): ...

class ScopedRegistry:
    createfunc: Any
    scopefunc: Any
    registry: Any
    def __init__(self, createfunc, scopefunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj) -> None: ...
    def clear(self) -> None: ...

class ThreadLocalRegistry(ScopedRegistry):
    createfunc: Any
    registry: Any
    def __init__(self, createfunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj) -> None: ...
    def clear(self) -> None: ...

def has_dupes(sequence, target): ...
