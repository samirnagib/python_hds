SELECT DISTINCT
    inputbill.ib_ano_mes AS 'Referencia',
    clientes.clientName AS 'Cliente',
    clientes.clientHostname AS 'Hostname',
    billtags.billtagName AS 'Camada de Consumo',
    billtags.billPriceTB AS 'Preço da camada',
    inputbill.cv_agent AS 'Tipo de Agente de Backup',
    inputbill.cv_subclient AS 'Job de Backup',
    inputbill.ib_taxcalculated AS 'Valor da Faixa',
    ((inputbill.cv_febackupsize) + (inputbill.cv_fearchivesize) + (inputbill.cv_primaryappsize) + (inputbill.cv_protectedappsize) + (inputbill.cv_mediasize)) AS 'TB acumulado',
    
    owner.owAR AS 'AR',
    owner.owName AS 'Responsável pelo ativo',
    owner.owProjectArea AS 'Projeto ou àrea'
FROM
    inputbill
        INNER JOIN
    billtags ON inputbill.id_billTag = billtags.idbillTag
        INNER JOIN
    clientes ON inputbill.id_client = clientes.idClient
        INNER JOIN
    clienttype ON clientes.idType = clienttype.idType
        INNER JOIN
    owner ON clientes.idOwner = owner.idOwner
WHERE
    ib_ano_mes = 'AGO 2022';  
