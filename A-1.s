	.file	"A-1.c"
	.text
	.comm	Z, 4, 2
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$64, %rsp
	.seh_stackalloc	64
	.seh_endprologue
	call	__main
	movl	$6, -4(%rbp)
	movl	$10, -8(%rbp)
	movl	$20, -12(%rbp)
	movl	-8(%rbp), %eax
	imull	-12(%rbp), %eax
	addl	$25, %eax
	movl	%eax, -16(%rbp)
	movl	$6, -4(%rbp)
	leaq	Z(%rip), %rax
	movl	(%rax), %eax
	movl	%eax, -20(%rbp)
	movsd	.LC0(%rip), %xmm0
	movsd	%xmm0, -32(%rbp)
	movsd	-32(%rbp), %xmm0
	cvttsd2sil	%xmm0, %edx
	leaq	Z(%rip), %rax
	movl	%edx, (%rax)
	leaq	Z(%rip), %rax
	movl	(%rax), %eax
	leal	1(%rax), %edx
	leaq	Z(%rip), %rax
	movl	%edx, (%rax)
	nop
	addq	$64, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
	.align 8
.LC0:
	.long	0
	.long	1078018048
	.ident	"GCC: (GNU) 9.2.0"
