left 90
pendown
:m = 20
repeat 5 [
	repeat 2 [
		repeat 4 [
			forward :m
			right 45
		]
	]
	repeat 2 [
		repeat 4 [
			forward :m
			left 45
		]
	]
	:m = :m+5
]