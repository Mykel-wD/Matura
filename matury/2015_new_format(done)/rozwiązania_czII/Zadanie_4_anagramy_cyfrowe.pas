program AnagramyCyfrowe;

{**
 * zamiana dodatniej liczby calkowitej k na najwiekszy jej anagram cyfrowy
 *}

function NajwiekszyAnagram(k: longint): longint;
var
  cyfry: array[0..9] of integer;
  cyfra, i, j: integer;
  wynik: longint;
begin
  for i := 0 to 9 do cyfry[i] := 0;
  while k <> 0 do
  begin
    cyfra := k mod 10;
    cyfry[cyfra] := cyfry[cyfra] + 1;
    k := k div 10
  end;
  wynik := 0;
  for i := 9 downto 0 do
    for j := 1 to cyfry[i] do
      wynik := wynik * 10 + i;
  NajwiekszyAnagram := wynik
end;

{**
 * struktura danych umozliwiajaca obliczenie maksymalnej liczby liczb, ktore
 * wzajemnie sa swoimi anagramami
 * anagramy[1..2001] - tablica zawieraj¹ca dotychczas odkryte, rozne anagramy
 * liczba_anagramow - liczba dotychczas odkrytych roznych anagramow
 * liczba_wystapien[1..2000] - liczba_wystapien[i] = liczbie dotychczasowych
 * wystapien anagramu anagramy[i]
 *}
var
  anagramy: array [1..2001] of longint;
  liczba_wystapien: array [1..2000] of integer;
  liczba_anagramow: integer;

procedure Ini;
var
  i: integer;
begin
  for i := 1 to 2000 do
    liczba_wystapien[i] := 0;
  liczba_anagramow := 0;
end;

function Ile(a: longint): integer;
{**
 * ile razy dotychczas pojawil sie anagram a
 *}
var
  i: integer;
begin
  anagramy[liczba_anagramow + 1] := a; {* wartownik *}
  i := 1;
  while anagramy[i] <> a do
    i := i + 1;
  liczba_wystapien[i] := liczba_wystapien[i] + 1;
  if i = liczba_anagramow + 1 then
    liczba_anagramow := i;
  Ile := liczba_wystapien[i]
end;

{**
 * program glowny
 *}

var
  u, v: longint;
  maksimum, wystapienia, wiersze_z_anagramami: integer;
  dane_anagramy: text;
begin
  maksimum := 0;
  wiersze_z_anagramami := 0;
  Ini;
  assign(dane_anagramy, 'dane_anagramy.txt');
  reset(dane_anagramy);
  writeln('1');
  while not eof(dane_anagramy) do
  begin
    readln(dane_anagramy, u, v);
    u := NajwiekszyAnagram(u);
    v := NajwiekszyAnagram(v);
    if u = v then
      wiersze_z_anagramami := wiersze_z_anagramami + 1;
    wystapienia := Ile(u);
    if wystapienia > maksimum then maksimum := wystapienia;
    wystapienia := Ile(v);
    if wystapienia > maksimum then maksimum := wystapienia
  end;
  close(dane_anagramy);
  writeln('wiersze z anagramami: ', wiersze_z_anagramami);
  writeln('maksimum anagramow: ', maksimum);
  readln
end.
