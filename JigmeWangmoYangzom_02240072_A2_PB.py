class PokemonBinder:
    def __init__(self):
        self.binder = {}  
        self.Max_PokeDex = 1025
        self.Cards_Per_BinderPage = 64
        self.row = 8
        self.coloumn = 8

    def calculate_page(self, number):                                          # to calculate the page number of the card in the binder
        cards_per_page = self.Cards_Per_BinderPage
        index = number - 1                                                     # subtracted 1 to get 0 based index which is pefered by python
        page = index // cards_per_page + 1                                     # added 1 to get the page number starting from 1
        return page

    def calculate_position(self, pokedex_number):                               # to calculate the position of the card in the binder page
        card_index_on_page = (pokedex_number - 1) % self.Cards_Per_BinderPage   # subtracted 1 to get 0 based index which is pefered by python         
        position = card_index_on_page + 1                                       # to get the position of the card on the binder page
        row = (position - 1) // 8 + 1                                           # divided by 8 since there is a total of 8 rows
        col = (position - 1) % 8 + 1                                            
        return row, col

    def add_card(self):
        number = int(input("Enter a Pokedex number (1 - 1025): "))              # to add pokemon card to a binder
        if number < 1 or number > self.Max_PokeDex:
            print("Invalid number. Must be between 1 and 1025.")
            return
        if number in self.binder:                                               #if the card already in the binder
            page, row, col = self.binder[number]
            print(f"Card already exists. Page: {page}, Row: {row}, Column: {col}")   
        else:
            page = self.calculate_page(number)
            row, col = self.calculate_position(number)
            self.binder[number] = (page, row, col)
            print(f"Card added to Page {page}, Row {row}, Column {col}")
        choice = input("Do you want to add another card? (yes or no): ")
        if choice.lower() == "yes":
            self.add_card()
        else:
            self.play_game()
        

    def reset_binder(self):
        confirm = input("Are you sure you want to RESET!: ")
        if confirm.upper() == "Yes" or "yes":
            self.binder.clear()
            print("Binder has been reset.")
        else:
            print("Reset cancelled.")
        self.cohoice = input("Do you want to go back to main menu (yes or no): ")
        if self.cohoice.lower() == "yes":
            print("Returning to the main menu.")
            self.play_game()
        else:
            self.exit()

    def show_summary(self):
        total_pokedex = self.Max_PokeDex
        current_cards = len(self.binder)
        percent_complete = (current_cards / total_pokedex) * 100

        print("--- Binder Summary ---")
        print(f"Total number of Pokémon in the Pokédex: {total_pokedex}")
        print(f"Total number of slots available in the binder: {total_pokedex}")
        print(f"Current number of cards in the binder: {current_cards}")
        print(f"Percentage of cards collected: {percent_complete:.2f}%")                # 2f so that the percentage is in 2 decimal format

        if current_cards == total_pokedex:
            print("You have caught them all!")

        print("Cards in Binder (Pokedex Number : Page Number, Row, Column)")
        print("-----------------------------------------------------------")
        for number in sorted(self.binder):
            page, row, col = self.binder[number]
            print(f"{number} : Page {page}, Row {row}, Column {col}")
        
        self.cohoice = input("Do you want to go back to main menu (yes or no): ")
        if self.cohoice.lower() == "yes":
            print("Returning to the main menu.")
            self.play_game()
        else:
            self.exit()

    def exit(self):
        print("Exiting the game. Thank you for playing!")
        exit()

    def play_game(self):
        while True:
            print()
            print("--- Pokemon Binder Menu ---")
            print("1. Add a card")
            print("2. Reset binder")
            print("3. Show summary")
            print("4. Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.add_card()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.show_summary()
            elif choice == "4":
                self.exit()
            break           

binder = PokemonBinder()
binder.play_game()
binder.calculate_page(1)  
binder.calculate_position(1)  
binder.add_card()  
binder.reset_binder()  
binder.show_summary()
binder.exit()


