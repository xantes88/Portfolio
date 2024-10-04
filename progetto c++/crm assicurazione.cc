#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <fstream>
#include <sstream>

// Struttura per memorizzare i clienti
struct Customer {
    int id;
    std::string name;
    std::string email;
    std::vector<std::string> interactions;
};

// Funzione di validazione del nome
bool isValidName(const std::string& name) {
    size_t spaceCount = 0;
    for (char c : name) {
        if (!std::isalpha(c) && c != ' ') {
            return false;
        }
        if (c == ' ') {
            ++spaceCount;
        }
    }
    
    // Deve esserci esattamente uno spazio
    if (spaceCount != 1) {
        return false;
    }
    
    // Verifica che ci siano due parti con solo lettere
    size_t spacePos = name.find(' ');
    std::string firstName = name.substr(0, spacePos);
    std::string lastName = name.substr(spacePos + 1);

    if (firstName.empty() || lastName.empty()) {
        return false;
    }

    for (char c : firstName) {
        if (!std::isalpha(c)) {
            return false;
        }
    }

    for (char c : lastName) {
        if (!std::isalpha(c)) {
            return false;
        }
    }

    return true;
}

// Funzione per ottenere un ID intero valido
int getValidID() {
    std::string input;
    int id;
    while (true) {
        std::cout << "Inserisci ID cliente (solo numeri interi): ";
        std::getline(std::cin, input);

        std::stringstream ss(input);
        if ((ss >> id) && (ss.eof())) { // Verifica se l'input è un intero e se non ci sono caratteri rimanenti nella stringa
            return id;
        } else {
            std::cout << "Input non valido. Per favore, inserisci un numero intero.\n";
        }
    }
}

// Funzione di validazione dell'email
bool isValidEmail(const std::string& email) {
    size_t atPos = email.find('@');
    if (atPos == std::string::npos) {
        return false; // Manca il simbolo @
    }

    std::string domain = email.substr(atPos + 1);
    if (domain.empty() || domain.find('.') == std::string::npos || domain.substr(domain.find_last_of('.')) != ".com") {
        return false; // Manca il dominio o il dominio non termina con .com
    }

    return true;
}

// Aggiungi un cliente
void addCustomer(std::vector<Customer>& customers) {
    int id = getValidID();
    std::string name, email;

    do {
        std::cout << "Inserisci nome completo del cliente (nome e cognome separati da uno spazio): ";
        std::getline(std::cin, name);
        if (!isValidName(name)) {
            std::cout << "Nome non valido. Assicurati di inserire solo lettere con un singolo spazio tra nome e cognome.\n";
        }
    } while (!isValidName(name));

    do {
        std::cout << "Inserisci email cliente: ";
        std::getline(std::cin, email);
        if (!isValidEmail(email)) {
            std::cout << "Email non valida. Assicurati che contenga il simbolo '@' e termini con '.com'.\n";
        }
    } while (!isValidEmail(email));

    customers.push_back({id, name, email});
    std::cout << "Cliente aggiunto con successo!\n";
}

// Visualizza tutti i clienti
void viewCustomers(const std::vector<Customer>& customers) {
    for (const auto& customer : customers) {
        std::cout << "ID: " << customer.id << ", Nome: " << customer.name << ", Email: " << customer.email << std::endl;
        for (const auto& interaction : customer.interactions) {
            std::cout << "  Interazione: " << interaction << std::endl;
        }
    }
}

// Modifica un cliente
void editCustomer(std::vector<Customer>& customers) {
    int id;
    std::cout << "Inserisci ID del cliente da modificare: ";
    std::cin >> id;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    for (auto& customer : customers) {
        if (customer.id == id) {
            std::string name, email;
            std::cout << "Inserisci nuovo nome completo del cliente (lascia vuoto per non modificare): ";
            std::getline(std::cin, name);
            if (!name.empty()) {
                if (isValidName(name)) {
                    customer.name = name;
                } else {
                    std::cout << "Nome non valido. Modifica non effettuata.\n";
                }
            }
            std::cout << "Inserisci nuova email del cliente (lascia vuoto per non modificare): ";
            std::getline(std::cin, email);
            if (!email.empty()) {
                if (isValidEmail(email)) {
                    customer.email = email;
                } else {
                    std::cout << "Email non valida. Modifica non effettuata.\n";
                }
            }
            std::cout << "Cliente modificato con successo!\n";
            return;
        }
    }
    std::cout << "Cliente non trovato.\n";
}

// Elimina un cliente
void deleteCustomer(std::vector<Customer>& customers) {
    int id;
    std::cout << "Inserisci ID del cliente da eliminare: ";
    std::cin >> id;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    for (auto it = customers.begin(); it != customers.end(); ++it) {
        if (it->id == id) {
            customers.erase(it);
            std::cout << "Cliente eliminato con successo!\n";
            return;
        }
    }
    std::cout << "Cliente non trovato.\n";
}

// Cerca un cliente per nome o cognome
void searchCustomer(const std::vector<Customer>& customers) {
    std::string name;
    std::cout << "Inserisci nome o cognome del cliente da cercare: ";
    std::getline(std::cin, name);

    for (const auto& customer : customers) {
        if (customer.name.find(name) != std::string::npos) {
            std::cout << "ID: " << customer.id << ", Nome: " << customer.name << ", Email: " << customer.email << std::endl;
            for (const auto& interaction : customer.interactions) {
                std::cout << "  Interazione: " << interaction << std::endl;
            }
        }
    }
}

// Aggiungi un'interazione per un cliente
void addInteraction(std::vector<Customer>& customers) {
    if (customers.empty()) {
        std::cout << "Nessun cliente disponibile per aggiungere un'interazione.\n";
        return;
    }

    int id;
    std::cout << "Inserisci ID del cliente per aggiungere un'interazione: ";
    std::cin >> id;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    bool customerFound = false;
    for (auto& customer : customers) {
        if (customer.id == id) {
            customerFound = true;
            std::string interaction;
            std::cout << "Inserisci dettagli dell'interazione: ";
            std::getline(std::cin, interaction);
            customer.interactions.push_back(interaction);
            std::cout << "Interazione aggiunta con successo!\n";
            return;
        }
    }

    if (!customerFound) {
        std::cout << "Cliente non trovato.\n";
    }
}

// Salva i dati su file
void saveData(const std::vector<Customer>& customers) {
    std::ofstream file("crm_data.txt");
    if (file.is_open()) {
        for (const auto& customer : customers) {
            file << customer.id << "," << customer.name << "," << customer.email << "\n";
            for (const auto& interaction : customer.interactions) {
                file << "interaction:" << interaction << "\n";
            }
        }
        file.close();
        std::cout << "Dati salvati con successo!\n";
    } else {
        std::cout << "Errore nell'apertura del file.\n";
    }
}

// Carica i dati da file
void loadData(std::vector<Customer>& customers) {
    std::ifstream file("crm_data.txt");
    if (file.is_open()) {
        customers.clear();
        std::string line;

        while (std::getline(file, line)) {
            std::cout << "Reading line: " << line << "\n"; // Debug message

            if (line.find("interaction:") == 0) {
                if (!customers.empty()) {
                    customers.back().interactions.push_back(line.substr(12));
                } else {
                    std::cerr << "Errore: Interazione trovata senza cliente associato.\n";
                }
            } else {
                std::istringstream iss(line);
                std::string id, name, email;
                std::getline(iss, id, ',');
                std::getline(iss, name, ',');
                std::getline(iss, email, ',');

                if (!id.empty() && !name.empty() && !email.empty()) {
                    customers.push_back({std::stoi(id), name, email});
                } else {
                    std::cerr << "Errore: Dato cliente malformato.\n";
                }
            }
        }
        file.close();
        std::cout << "Dati caricati con successo!\n";
    } else {
        std::cout << "Errore nell'apertura del file.\n";
    }
}

int main() {
    std::vector<Customer> customers;

    // Carica i dati dei clienti e delle interazioni all'avvio
    loadData(customers);

    int choice;
    do {
        std::cout << "\nMenu CRM:\n";
        std::cout << "1. Aggiungi Cliente\n";
        std::cout << "2. Visualizza Clienti\n";
        std::cout << "3. Modifica Cliente\n";
        std::cout << "4. Elimina Cliente\n";
        std::cout << "5. Cerca Cliente\n";
        std::cout << "6. Aggiungi Interazione\n";
        std::cout << "7. Salva e Esci\n";
        std::cout << "Scegli un'opzione: ";
        std::cin >> choice;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignoriamo il resto della linea

        switch (choice) {
            case 1:
                addCustomer(customers);
                break;
            case 2:
                viewCustomers(customers);
                break;
            case 3:
                editCustomer(customers);
                break;
            case 4:
                deleteCustomer(customers);
                break;
            case 5:
                searchCustomer(customers);
                break;
            case 6:
                addInteraction(customers);
                break;
            case 7:
                saveData(customers);
                std::cout << "Uscita...\n";
                break;
            default:
                std::cout << "Opzione non valida.\n";
                break;
        }
    } while (choice != 7);

    return 0;
}


