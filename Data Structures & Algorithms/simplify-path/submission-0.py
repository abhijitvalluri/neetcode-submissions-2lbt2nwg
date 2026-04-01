class Solution:
    def simplifyPath(self, path: str) -> str:
        path_components = path.split("/")
        canonical_components = []

        for comp in path_components:
            if comp == ".." and canonical_components:
                canonical_components.pop()
            elif comp not in {".", "..", ""}:
                canonical_components.append(comp)
        
        return "/" + "/".join(canonical_components)