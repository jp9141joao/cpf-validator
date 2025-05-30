# **CPF Validator**

This is a simple Python program that validates the authenticity of a Brazilian CPF (Cadastro de Pessoa Física). It calculates the two verification digits of a CPF and checks if they match the expected values, confirming whether the provided CPF is valid or invalid.

---

## **Features**

* **CPF Validation:** The program validates an entered CPF number by verifying the consistency of its last two verification digits.
* **Invalid CPF Detection:** The program detects CPFs with an invalid number of characters or that fail the verification digit calculations.

---

## **How to Use**

1. Run the program in the terminal.
2. The program will prompt you to enter a CPF number.
3. After entering the CPF, the program will verify the validity of the two verification digits and inform you whether the CPF is **valid** or **invalid**.

---

## **Example of Execution**

When running the code, it will prompt for the CPF to validate:

```
Enter your CPF: 12345678909
```

The program will then display the following message depending on the CPF provided:

```
Invalid CPF!
```

Or, if the CPF is valid:

```
Valid CPF!
```

---

## **Requirements**

* **Python 3.x:** The code was developed to run on recent versions of Python.

---

## **How to Run**

1. Make sure Python 3 is installed on your system.
2. Download the source code and save it in a file named `validador_cpf.py`.
3. Open the terminal and navigate to the directory where the file is saved.
4. Run the command:

```bash
python validador_cpf.py
```

---

## **Notes**

* The program accepts an 11-digit CPF and performs calculations based on the last two digits, which are responsible for validating the CPF.
* The code does not perform CPF formatting (it does not accept dots or dashes), so the CPF must be entered without any separator characters.

---

Enjoy validating your CPFs! 🎉
