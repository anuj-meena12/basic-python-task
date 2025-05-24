def main():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    full_name = f"{first_name} {last_name}"
    print(f"\nHello, {full_name}! Welcome to the Python world.")

if __name__ == "__main__":
    main()
