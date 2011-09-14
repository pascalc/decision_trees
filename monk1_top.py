import dtree as d
import monkdata as m
import drawtree as dt

def isLeaf(subset):
	return d.allPositive(subset) or d.allNegative(subset)

def buildTree(subset,attrs):
	global tree
	if isLeaf(subset):
		tree = (tree + '+') if d.allPositive(subset) else (tree + '-')
		return
	else:
		root = d.bestAttribute(subset,attrs)
		tree = tree + str(root) + "("
		for value in root.values:
			nextSubset = d.select(subset,root,value)
			nextAttrs = attrs - set([root])
			buildTree(nextSubset,nextAttrs)
		tree = tree + ")"

tree = ""

buildTree(m.monk1,set(m.attributes))

#dt.drawTree(tree)
id3tree = d.buildTree(m.monk1,m.attributes)
dt.drawTree(id3tree)