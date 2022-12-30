frozen_set_1={'C', 'A', 'B', 'D'}
frozen_set_2={2, 'A', 'C', 4}
frozenset_union=frozen_set_1.union(frozen_set_2)
print(frozenset_union)
frozenset_common=frozen_set_1.intersection(frozen_set_2)
print(frozenset_common)
frozenset_difference=frozen_set_1.difference(frozen_set_2)
print(frozenset_difference)
frozenset_distinct=frozenset_union-frozenset_common
print(frozenset_distinct)