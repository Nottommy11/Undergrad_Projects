.data
	prompt:		.asciiz "Enter a float value for the Width (in feet) of your frame: "
		
	output1:	.asciiz "\nYou will need, "
	output2:	.asciiz " feet for your frame length to observe the Golden Ratio."

	floatZero:	.float 0.0
	goldenRatio:	.float 1.618

.text
	main:
		lwc1 $f1, floatZero
		lwc1 $f2, goldenRatio
		
		li $v0, 4
		la $a0, prompt
		syscall
		
		li $v0, 6
		syscall
		
		jal printResults
		
		li $v0, 10
		syscall
	
	printResults:
		li $v0, 4
		la $a0, output1
		syscall
		
		li $v0, 2
		mul.s $f12, $f0, $f2
		syscall
		
		li $v0, 4
		la $a0, output2
		syscall
		
		jr $ra
