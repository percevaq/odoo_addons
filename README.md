###odoo_addons
####Addons for Odoo/OpenERP by Joaquin Gutierrez Pedrosa
---

<dl>
<dt>fix_pos_pricelist_tax</dt>
<dd>
Al instalar la nueva version de pos_pricelist. Se crean unos campos para el 
desglose de impuestos. Dichos campos no se rellenan cuando hacemos los 
pedidos desde el BackEnd.
Este modulo soluciona el problema.
</dd>

<dt>l10n_es_hr_payroll</dt>
<dd>
Agrega los campos seguridad social del trabajador, seguridad social de la empresa
y % de retencion IRPF a los contratos.
Crea las reglas necesarias para el calculo de la nomina para la localizacion española.
</dd>
<dt>l10n_es_hr_payroll_account</dt>
<dd>
Mapea las cuentas contables necesarias a cada regla salarial para la contabilizacion
de las nominas.
Se debe crear un diario de tipo compra y agregar como cuenta acreedora y deudora
465xxx
</dd>
<dt>hr_payroll_payment_order</dt>
<dd>
Crea una orden de pago con las nominas asociadas a un procesado de nominas.
Se puede usar con la exportacion SEPA para el envio de las transferencias.
</dd>
<dt>hr_payroll_advance</dt>
<dd>
Gestion de anticipos de nomina.
</dd>
<dt>document_icon</dt>
<dd>
Agrega una tabla con mimetypes, extensiones de fichero e iconos para 
cambiar la forma en la que se representan los ir.attachment en el sistema
</dd>
</dl>