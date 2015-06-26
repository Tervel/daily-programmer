def invertTree(self, rootNode):
    if rootNode is not None:
        temp = rootNode.left
        rootNode.left = self.invertTree(rootNode.right)
        rootNode.right = self.invertTree(temp)

    return rootNode