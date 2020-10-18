
def in_set(user_set, user_input):
    if user_input in user_set:
        return True
    else:
        return False

if __name__ == "__main__":
    print(in_set({3,5,8,9}, 3))