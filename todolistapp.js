

var todos = ["Buy New Turtle"];

var input = prompt("What would you like to do?");




while (input !== "quit"){

	//handle input

if (input === "list"){
	console.log(todos);
} else if (input === "new"){
	//ask user for new todo 
	var newTodo = prompt ("Enter new todo");
	//add to todos array
	todos.push(newTodo);
	}
	//ask again for new input
	 input = prompt("What would you like to do?");

}

if (input == "quit"){
	var input2 = prompt("Are you sure you want to quit?");
		if (input2 == "no"){
		input = prompt("What would you like to do?");
	} else if (input2 == "yes") {
		alert("You Quitter!");
		console.log("User quit application");
	}
}