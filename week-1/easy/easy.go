// create a program that will ask the users name, age, and reddit username.
// have it tell them the information back, in the format:
// your name is (blank), you are (blank) years old, and your username is (blank)
// for extra credit, have the program log this information in a file to be
// accessed later.

package main

import "fmt"

func main() {
	var name string
	var age string
	var username string

	fmt.Print("Enter name: ")
	fmt.Scanln(&name)

	fmt.Print("Enter age: ")
	fmt.Scanln(&age)

	fmt.Print("Enter username: ")
	fmt.Scanln(&username)

	fmt.Printf("your name is %s, you are %s years old, and your username is %s", name, age, username)

	fmt.Scanln()
}
