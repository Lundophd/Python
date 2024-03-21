
salario_neto =int(input("Ingrese su salario"));
valor_contructivo = 0.4*salario_neto;

salud = valor_contructivo*0.125;

pension = valor_contructivo*0.16;

total_pago = salario_neto-salud-pension;

print (total_pago);
print (f"el empleado tiene como salario neto {salario_neto}, y se le descuenta {salud}por salud y {pension} por pension, recibiendo un salario de {total_pago}.");

