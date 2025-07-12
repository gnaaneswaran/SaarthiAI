from agents.saarthi_agent import handle_query

def main():
    print("Welcome to SaarthiAI CLI")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        print("SaarthiAI:", handle_query(query))

if __name__ == "__main__":
    main()
