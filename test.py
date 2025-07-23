from pddl2hoa import convert_pddl_to_hoa

state_labeled, edge_labeled, strategy = convert_pddl_to_hoa('pddl/hanoi.pddl', 'pddl/hanoi/problem0.pddl')
print(state_labeled)
print(edge_labeled)
print(strategy)