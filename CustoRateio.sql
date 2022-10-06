SELECT DISTINCT
    ib_ano_mes AS 'Referencia',
    clientName AS 'Cliente',
    clientes.clientHostname AS 'Hostname',
    billTags.billtagName AS 'Camada de Consumo',
    billTags.billPriceTB AS 'Preço da camada',
    inputBill.cv_agent AS 'Tipo de Agente de Backup',
    inputBill.cv_subclient 'Job de Backup',
    inputBill.ib_taxcalculated AS 'Valor da Faixa',
    ((inputbill.cv_febackupsize) + (inputbill.cv_fearchivesize) + (inputbill.cv_primaryappsize) + (inputbill.cv_protectedappsize) + (inputbill.cv_mediasize)) AS 'TB acumulado',
    owner.owAR AS 'AR',
    owner.owName AS 'Responsável pelo ativo',
    owner.owProjectArea AS 'Projeto ou àrea'
FROM
    inputBill
        INNER JOIN
    billTags ON inputBill.id_billTag = billTags.idbillTag
        INNER JOIN
    clientes ON inputBill.id_client = clientes.idClient
        INNER JOIN
    clientType ON clientes.idType = clientType.idType
        INNER JOIN
    owner ON clientes.idOwner = owner.idOwner
WHERE
    ib_ano_mes = 'AGO 2022';


10:48:20	inputBill.	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'inputBill.' at line 1	0.000 sec
