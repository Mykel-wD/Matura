#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>

/**
 * zamiana dodatniej liczby calkowitej k na najwiekszy jej anagram cyfrowy
 */
int najwiekszy_anagram(int k){
    int cyfry[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    while (k != 0)
    {
        int cyfra = k % 10;
        cyfry[cyfra]++;
        k = k / 10;
    }
    int wynik = 0;
    for (int i = 9; i >= 0; i--)
        for (int j = 0; j < cyfry[i]; j++)
            wynik = wynik * 10 + i;
    return wynik;
}

std::map<int, int> anagramy;
int wiersze_z_anagramami;
int maksimum;

int main() {
    int u, v;
    std::ifstream liczba("dane_anagramy.txt");
    while (liczba >> u >> v)
    {
        int anagram_u = najwiekszy_anagram(u);
        int anagram_v = najwiekszy_anagram(v);
        if (anagram_u == anagram_v)
            wiersze_z_anagramami++;
        anagramy[anagram_u]++;
        anagramy[anagram_v]++;
        maksimum = std::max(maksimum, anagramy[anagram_u]);
        maksimum = std::max(maksimum, anagramy[anagram_v]);
    }
    std::cout << "wiersze z anagramami: " << wiersze_z_anagramami <<
        std::endl;
    std::cout << "maksimum anagramow: " << maksimum << std::endl;
    return 0;
}
