import sys

if __name__ == "__main__":
    with open("dog_breeds.txt", "a") as f:
        f.writelines(f"\nArguments count: {len(sys.argv)}")
        for i, arg in enumerate(sys.argv):
            f.writelines(f"\nArgument {i:>6}: {arg}")