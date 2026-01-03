def main():
    scores = [78, 77, 85, 66, 65]
    total = sum(scores)
    average = total / len(scores)
    print("== main/master branch ==")
    print(f"scores: {scores}")
    print(f"sum: {total}")
    print(f"average: {average}")
    
if __name__ == "__main__":
    main()

