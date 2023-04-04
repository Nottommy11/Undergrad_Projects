.data
	selectionPrompt: .asciiz "\nWould you like to encrypt or exit?\n(\"0\" to ENCRYPT OR \"1\" to EXIT): "
	
	encryptPrompt: .asciiz "Enter a character: "
	
	notFound: .asciiz "That character was not found!\n"
	
	exitPrompt: .asciiz "Goodbye, see you soon!"
	
	alpha: .asciiz "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	newLine: .asciiz "\n"
	
	binary: .space 32
	
	userInput: .byte

.text
	main:
	
		mul $t0, $t0, 0
		mul $t1, $t0, 0
		mul $t2, $t0, 0
		mul $t3, $t0, 0
		mul $a0, $t0, 0
		mul $a1, $t0, 0
		mul $s0, $t0, 0
		mul $s1, $t0, 0
		mul $s2, $t0, 0
	
		li $v0, 4
		la $a0, selectionPrompt
		syscall
		
		li $v0, 5 # Take integer input
         	syscall
         	
         	# Move Integer input into t0
         	move $t0, $v0
         	
         	# If branch based on input
         	# 0 for encryption of input
         	beq $t0, $zero, encryptPath
         	# 1 for ending the program
         	beq $t0, 2, exitProgram
		
		
	exitProgram:
		li $v0, 4
		la $a0, exitPrompt
		syscall
		
		# Exit program
		li $v0, 10
		syscall
		
	binaryStore:
		beq $t1, 32, binaryPrint
		div $s1, $s1, 2
		mfhi $s2
		sb $s2, binary($t1)
		addi $t1, $t1, 4
		mul $t0, $t0, 0
		j binaryStore
		
	binaryPrint:
		beq $t0, -32, main
		addi $t3, $t0, 28
		li $v0, 1
		lb $a0, binary($t3)
		addi $t0, $t0, -4
		syscall
		j binaryPrint

	encryptPath:
		li $v0, 4
		la $a0, encryptPrompt
		syscall
		
		# Take String input
		li $v0, 12
		syscall
		
		sb $v0, userInput
		lb $s0, userInput
		
		li $v0, 4
		la $a0, newLine
		syscall
		la $a0, userInput
		syscall
		la $a0, newLine
		syscall
		
		# Loop through alphabet
		loop:
			# Counter
			beq $t0, 26, alphaNotFound
	
			lb $s1, alpha($t0)
			
			# Search for char one by one in array
			beq $s0, $s1, binaryStore
					
			addi $t0, $t0, 1
			j loop
	
	alphaNotFound:
		li $v0, 4
		la $a0, notFound
		syscall
		
		j main
