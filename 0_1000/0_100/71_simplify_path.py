class Solution:
    def simplify_path(self, path):
        tree = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if len(tree) > 0:
                    tree.pop()
            else:
                tree.append(part)

        return "/" + "/".join(tree)

print(Solution().simplify_path(path = "/home/"))
print(Solution().simplify_path(path = "/home//foo/"))
print(Solution().simplify_path(path = "/home/user/Documents/../Pictures"))
print(Solution().simplify_path(path = "/../"))
print(Solution().simplify_path(path = "/.../a/../b/c/../d/./"))
print(Solution().simplify_path(path = "/a/./b/../../c/"))
