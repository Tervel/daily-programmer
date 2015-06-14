package main

import "fmt"
import "math/rand"
import "time"

func random(max int, min int) int {
	rand.Seed(time.Now().UnixNano()) // Generate current unix time(to nanoseconds), and use it to seed time

	return rand.Intn(max-min) + min // return random number within range
}

func main() {
	var number int
	var guess int
	high := 100
	low := 1

	number = random(high, low)
	fmt.Print(number)

	for guess != number {
		fmt.Print("Your Guess: ")
		fmt.Scanf("%d\n", &guess)
	}

	fmt.Printf("Your guess of %d was correct!", guess)
	fmt.Scanln()
}
