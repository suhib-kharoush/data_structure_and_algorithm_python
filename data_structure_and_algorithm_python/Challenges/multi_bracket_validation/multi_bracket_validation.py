def matched(str):
    braces = {'{':'}','[':']','(':')'}
    stack = []
    for c in str:
        if c in braces.keys():
            stack.append(c)
        elif c in braces.values():
            if not stack:
                return False
            close_brace = stack.pop()
            if braces[close_brace] !=c:
                return False
    if stack:
        return False
    return True

print(matched("()"))

print(matched("(}"))

print(matched("}{"))

print(matched("}"))

print(matched("{"))

print(matched("(ff{any} [code]h)"))