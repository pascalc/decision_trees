#!/usr/bin/env python

import dtree as d
import monkdata as m
from texttable import Texttable

monkdata = [m.monk1,m.monk2,m.monk3]
testdata = [m.monk1test,m.monk2test,m.monk3test]

# Assignment 1
def assignment1():
	print "--- Assignment 1 ---"
	print "Initial entropy of the datasets"
	table = Texttable(max_width=100)
	table.add_row(["Dataset","Entropy"])
	for i in range(3):
		table.add_row(["Monk-" + str(i+1), d.entropy(monkdata[i])])
	print table.draw()
	print

# Assignment 2
def assignment2():
	print "--- Assignment 2 ---"
	print "Selecting the root of the decision tree"
	table = Texttable(max_width=100)
	table.add_row(["Dataset", "a1", "a2", "a3", "a4", "a5", "a6"])
	for i in range(3):
		gains = map(lambda att: d.averageGain(monkdata[i],att), m.attributes)
		table.add_row(["Monk-" + str(i+1)] + gains)
	print table.draw()
	print

# Assignment 3
def assignment3():
	print "--- Assignment 3 ---"
	print "Performance of the decision trees"
	table = Texttable(max_width=100)
	table.add_row(["Dataset", "Training", "Test"])
	for i in range(3):
		tree = d.buildTree(monkdata[i],m.attributes)
		perf = [d.check(tree, monkdata[i]), d.check(tree, testdata[i])]
		table.add_row(["Monk-" + str(i+1)] + perf)
	print table.draw()
	print
	
# Assignment 4
def assignment4():
	print "--- Assignment 4 ---"
	print "Selecting the best fraction to divide training and validation sets for pruning"
	def best_pruned(pruned,valid_set):
		best = (None,0)
		for tree in pruned:
			perf = d.check(tree,valid_set)
			if perf > best[1]:
				best = (tree, perf)
		return best
	
	table = Texttable(max_width=100)
	table.add_row(["Dataset", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "Full Tree"])
	for i in range(3):
		row = ["Monk-" + str(i+1)]
		for frac in [(x * 0.1) for x in range(3,9)]:
			train_set, valid_set = m.partition(monkdata[i], frac)
			base = d.buildTree(train_set,m.attributes)
			pruned = d.allPruned(base)
			best = best_pruned(pruned,valid_set)
			true_perf = d.check(best[0],testdata[i])
			row += [true_perf]
		row += [d.check(d.buildTree(monkdata[i],m.attributes),testdata[i])]
		table.add_row(row)
	print table.draw()
	print					
			
assignment1()
assignment2()
assignment3()
assignment4()