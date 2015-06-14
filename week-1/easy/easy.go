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
