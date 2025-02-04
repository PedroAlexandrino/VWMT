Started sentry with debug=True
->  enviarEmailSchedule
->  enviarEmailSchedule
->  enviarEmailSchedule
->  updateSchedule
->  updateLineRequestDia1
->  updatePortariaDia1
->  updatePortariaDia15
->  updateProductionDia1
->  updateICDRDia1
Foram adicionadas 20 rotas
[<URLPattern '' [name='armazem']>, <URLPattern 'armazem/tabelaParent' [name='armazem_tabelaParent']>, <URLPattern 'create/' [name='create']>, <URLPattern 'tabela/' [name='tabela']>, <URLPattern 'operations/' [name='operations']>, <URLPattern 'shippingOperation/' [name='shippingOperation']>, <URLPattern 'receivingOperation/' [name='receivingOperation']>, <URLPattern 'nonProductionOperation/' [name='nonProductionOperation']>, <URLPattern 'qpsPackingPage/' [name='qpsPackingPage']>, <URLPattern 'qpsPacking/' [name='qpsPacking']>, <URLPattern 'qpsShipping/' [name='qpsShipping']>, <URLPattern 'configurationShippingOperation/' [name='configurationShippingOperation']>, <URLPattern 'configurationReceivingOperation/' [name='configurationReceivingOperation']>, <URLPattern 'configurationCrossdockingOperation/' [name='configurationCrossdockingOperation']>, <URLPattern 'configurationDocumentacao/' [name='configurationDocumentacao']>, <URLPattern 'configurationAnexos/' [name='configurationAnexos']>, <URLPattern 'configurationQps/' [name='configurationQps']>, <URLPattern 'configurationOthers/' [name='configurationOthers']>, <URLPattern 'reportOperations' [name='reportOperations']>, <URLPattern 'reportNonProduction' [name='reportNonProduction']>]
--
-- Create model Abs2Priv
--
CREATE TABLE [shippers_abs2priv] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [abs_par_id_2] nvarchar(100) NULL, [abs_item_2] nvarchar(100) NULL, [abs_qty_2] nvarchar(100) NULL, [abs_ship_qty_2] nvarchar(100) NULL);
--
-- Create model AbsMstrPriv
--
CREATE TABLE [shippers_absmstrpriv] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [abs_id_2] nvarchar(100) NULL, [abs_shp_date_2] nvarchar(100) NULL, [abs_shp_time_2] nvarchar(100) NULL, [abs_qad01_2] nvarchar(150) NULL, [oid_abs_mstr_2] nvarchar(100) NULL, [abs_status_2] nvarchar(100) NULL, [abs_shipto_2] nvarchar(100) NULL, [abs_item_2] nvarchar(100) NULL, [abs_domain_2] nvarchar(100) NULL);
--
-- Create model ficheiroShippers
--
CREATE TABLE [shippers_ficheiroshippers] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [masterSerialID] nvarchar(50) NULL, [preShipperShipper] nvarchar(50) NULL, [packItem] nvarchar(50) NULL, [numberOfPacks] nvarchar(50) NULL);
--
-- Create model filteredTable
--
CREATE TABLE [shippers_filteredtable] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [idComum] nvarchar(50) NULL, [shipDate] nvarchar(50) NULL, [shipTime] nvarchar(50) NULL, [name] nvarchar(50) NULL, [city] nvarchar(50) NULL, [carrier] nvarchar(50) NULL, [modeOfTransport] nvarchar(50) NULL, [vehicleID] nvarchar(50) NULL, [itemNumber] nvarchar(50) NULL, [description] nvarchar(150) NULL, [quantityToShip] nvarchar(150) NULL, [quantityShipped] nvarchar(150) NULL, [inProcess] nvarchar(150) NULL, [confirmed] nvarchar(150) NULL);
--
-- Create model finalFicheiroShippers
--
CREATE TABLE [shippers_finalficheiroshippers] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [masterSerialID] nvarchar(50) NULL, [preShipperShipper] nvarchar(50) NULL, [packItem] nvarchar(50) NULL, [numberOfPacks] nvarchar(50) NULL);
--
-- Create model Gateway
--
CREATE TABLE [shippers_gateway] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [dataHoraChegada] nvarchar(100) NULL, [empresa] nvarchar(100) NULL, [condutor] nvarchar(100) NULL, [ident] nvarchar(100) NULL, [contacto] nvarchar(100) NULL, [primeiraMatricula] nvarchar(100) NULL, [segundaMatricula] nvarchar(100) NULL, [cargaDescarga] nvarchar(100) NULL, [doca] nvarchar(100) NULL, [destinoCarga] nvarchar(100) NULL, [tipoViatura] nvarchar(100) NULL, [dataHoraEntrada] nvarchar(100) NULL, [estado] nvarchar(100) NULL, [abandono] nvarchar(100) NULL, [comentEntrada] nvarchar(300) NULL, [dataHoraSaida] nvarchar(100) NULL, [comentSaida] nvarchar(300) NULL);
--
-- Create model GatewayBackup
--
CREATE TABLE [shippers_gatewaybackup] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [dataHoraChegada] nvarchar(100) NULL, [empresa] nvarchar(100) NULL, [condutor] nvarchar(100) NULL, [ident] nvarchar(100) NULL, [contacto] nvarchar(100) NULL, [primeiraMatricula] nvarchar(100) NULL, [segundaMatricula] nvarchar(100) NULL, [cargaDescarga] nvarchar(100) NULL, [doca] nvarchar(100) NULL, [destinoCarga] nvarchar(100) NULL, [tipoViatura] nvarchar(100) NULL, [dataHoraEntrada] nvarchar(100) NULL, [estado] nvarchar(100) NULL, [abandono] nvarchar(100) NULL, [comentEntrada] nvarchar(300) NULL, [dataHoraSaida] nvarchar(100) NULL, [comentSaida] nvarchar(300) NULL);
--
-- Create model GatewayCargaDescarga
--
CREATE TABLE [shippers_gatewaycargadescarga] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayCondutor
--
CREATE TABLE [shippers_gatewaycondutor] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayCondutorID
--
CREATE TABLE [shippers_gatewaycondutorid] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayContactoCondutor
--
CREATE TABLE [shippers_gatewaycontactocondutor] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayDestinoCarga
--
CREATE TABLE [shippers_gatewaydestinocarga] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayDoca
--
CREATE TABLE [shippers_gatewaydoca] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayEmpresa
--
CREATE TABLE [shippers_gatewayempresa] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewaySegundaMatricula
--
CREATE TABLE [shippers_gatewaysegundamatricula] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model GatewayTipoViatura
--
CREATE TABLE [shippers_gatewaytipoviatura] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model PreShipperBrowse
--
CREATE TABLE [shippers_preshipperbrowse] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [shipFrom] nvarchar(50) NULL, [type] nvarchar(50) NULL, [idShipper] nvarchar(50) NULL, [shipTo] nvarchar(50) NULL, [name] nvarchar(50) NULL, [city] nvarchar(50) NULL, [state] nvarchar(50) NULL, [country] nvarchar(50) NULL, [shipDate] nvarchar(50) NULL, [shipTime] nvarchar(50) NULL, [carrier] nvarchar(50) NULL, [shipVia] nvarchar(50) NULL, [fob] nvarchar(150) NULL, [transportMode] nvarchar(150) NULL, [vehicleId] nvarchar(150) NULL, [mbol] nvarchar(150) NULL, [preShipper] nvarchar(150) NULL, [totalMasterPacks] nvarchar(150) NULL, [loadedMasterPacks] nvarchar(150) NULL, [inProcess] nvarchar(150) NULL, [confirmed] nvarchar(150) NULL, [cancelled] nvarchar(150) NULL, [invMov] nvarchar(150) NULL);
--
-- Create model PreShipperDetailBrowse
--
CREATE TABLE [shippers_preshipperdetailbrowse] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [shipFrom] nvarchar(50) NULL, [type] nvarchar(50) NULL, [idShipper] nvarchar(50) NULL, [sortName] nvarchar(50) NULL, [shipTo] nvarchar(50) NULL, [shipToDock] nvarchar(50) NULL, [shipDate] nvarchar(50) NULL, [itemNumber] nvarchar(50) NULL, [description] nvarchar(50) NULL, [quantityToShip] nvarchar(50) NULL, [quantityShipped] nvarchar(50) NULL, [um] nvarchar(50) NULL, [site] nvarchar(50) NULL, [location] nvarchar(50) NULL, [lotSerial] nvarchar(150) NULL, [reference] nvarchar(150) NULL, [order] nvarchar(150) NULL, [line] nvarchar(150) NULL, [mbol] nvarchar(150) NULL, [confirmed] nvarchar(150) NULL, [invMov] nvarchar(150) NULL, [idGrande] nvarchar(150) NULL);
--
-- Create model Security
--
CREATE TABLE [shippers_security] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [shipper] nvarchar(100) NULL, [masterSerials] nvarchar(100) NULL, [validacao] nvarchar(100) NULL, [dataHoraSaida] nvarchar(100) NULL, [comentarios] nvarchar(100) NULL);
--
-- Create model SecurityShipper
--
CREATE TABLE [shippers_securityshipper] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL);
--
-- Create model Teste_browse
--
CREATE TABLE [shippers_teste_browse] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [shipFrom] nvarchar(50) NULL, [type] nvarchar(50) NULL, [idBrowse] nvarchar(50) NULL, [shipTo] nvarchar(50) NULL, [name] nvarchar(50) NULL, [city] nvarchar(50) NULL, [state] nvarchar(50) NULL, [country] nvarchar(50) NULL, [shipDate] nvarchar(50) NULL, [shipTime] nvarchar(50) NULL, [carrier] nvarchar(50) NULL, [shipVia] nvarchar(50) NULL, [fob] nvarchar(50) NULL, [modeOfTransport] nvarchar(50) NULL, [vehicleID] nvarchar(50) NULL, [mbol] nvarchar(50) NULL, [preShipperID] nvarchar(50) NULL, [totalMasterPacks] nvarchar(50) NULL, [loadedMasterPacks] nvarchar(50) NULL, [inProcess] nvarchar(50) NULL, [confirmed] nvarchar(150) NULL, [cancelled] nvarchar(150) NULL, [invMov] nvarchar(150) NULL);
--
-- Create model Teste_detail
--
CREATE TABLE [shippers_teste_detail] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [shipFrom] nvarchar(50) NULL, [type] nvarchar(50) NULL, [preShipperShipper] nvarchar(50) NULL, [sortName] nvarchar(50) NULL, [shipTo] nvarchar(50) NULL, [shipToDock] nvarchar(50) NULL, [shipDate] nvarchar(50) NULL, [itemNumber] nvarchar(50) NULL, [description] nvarchar(100) NULL, [quantityToShip] nvarchar(50) NULL, [quantityShipped] nvarchar(50) NULL, [um] nvarchar(50) NULL, [site] nvarchar(50) NULL, [location] nvarchar(50) NULL, [lotSerial] nvarchar(50) NULL, [reference] nvarchar(50) NULL, [order] nvarchar(50) NULL, [line] nvarchar(150) NULL, [mbol] nvarchar(150) NULL, [confirmed] nvarchar(150) NULL, [invMov] nvarchar(150) NULL, [idDetail] nvarchar(100) NULL);
--
-- Create model TrackingPage
--
CREATE TABLE [shippers_trackingpage] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nShipper] nvarchar(10) NULL, [qtyCaixas] nvarchar(15) NULL, [inicioPrep] date NULL, [fimPrep] datetime2 NULL, [confirmacao] datetime2 NULL, [comentarios] nvarchar(100) NULL, [ship_date] nvarchar(20) NULL, [ship_time] nvarchar(20) NULL, [ship_carrier] nvarchar(20) NULL);
--
-- Create model PtPriv
--
CREATE TABLE [shippers_ptpriv] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [pt_desc1_2] nvarchar(100) NULL, [pt_desc2_2] nvarchar(100) NULL, [pt_part_2_id] int NOT NULL);
--
-- Create model GatewayPrimeiraMatricula
--
CREATE TABLE [shippers_gatewayprimeiramatricula] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [nome] nvarchar(100) NULL, [empresa_id] int NULL);
--
-- Create model GatewayInfoCondutor
--
CREATE TABLE [shippers_gatewayinfocondutor] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [condutor_id] int NULL, [condutorID_id] int NULL, [contacto_id] int NULL, [empresa_id] int NULL);
--
-- Create model AdPriv
--
CREATE TABLE [shippers_adpriv] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [ad_city_2] nvarchar(100) NULL, [ad_country_2] nvarchar(100) NULL, [ad_addr_2_id] int NOT NULL);
--
-- Create model AbscPriv
--
CREATE TABLE [shippers_abscpriv] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [absc_carrier_2] nvarchar(100) NULL, [absc_abs_id_2_id] int NOT NULL);
CREATE INDEX [shippers_gatewayinfocondutor_contacto_id_9697d6c1] ON [shippers_gatewayinfocondutor] ([contacto_id]);
CREATE INDEX [shippers_abscpriv_absc_abs_id_2_id_663540f2] ON [shippers_abscpriv] ([absc_abs_id_2_id]);
ALTER TABLE [shippers_gatewayinfocondutor] ADD CONSTRAINT [shippers_gatewayinfocondutor_empresa_id_d57824b7_fk_shippers_gatewayempresa_id] FOREIGN KEY ([empresa_id]) REFERENCES [shippers_gatewayempresa] ([id]);
ALTER TABLE [shippers_abscpriv] ADD CONSTRAINT [shippers_abscpriv_absc_abs_id_2_id_663540f2_fk_shippers_abs2priv_id] FOREIGN KEY ([absc_abs_id_2_id]) REFERENCES [shippers_abs2priv] ([id]);
CREATE INDEX [shippers_gatewayinfocondutor_condutor_id_a3a03741] ON [shippers_gatewayinfocondutor] ([condutor_id]);
CREATE INDEX [shippers_gatewayinfocondutor_empresa_id_d57824b7] ON [shippers_gatewayinfocondutor] ([empresa_id]);
CREATE INDEX [shippers_adpriv_ad_addr_2_id_229f63ec] ON [shippers_adpriv] ([ad_addr_2_id]);
ALTER TABLE [shippers_ptpriv] ADD CONSTRAINT [shippers_ptpriv_pt_part_2_id_88a53124_fk_shippers_abs2priv_id] FOREIGN KEY ([pt_part_2_id]) REFERENCES [shippers_abs2priv] ([id]);
ALTER TABLE [shippers_adpriv] ADD CONSTRAINT [shippers_adpriv_ad_addr_2_id_229f63ec_fk_shippers_absmstrpriv_id] FOREIGN KEY ([ad_addr_2_id]) REFERENCES [shippers_absmstrpriv] ([id]);
CREATE INDEX [shippers_gatewayinfocondutor_condutorID_id_5ce55aa0] ON [shippers_gatewayinfocondutor] ([condutorID_id]);
ALTER TABLE [shippers_gatewayinfocondutor] ADD CONSTRAINT [shippers_gatewayinfocondutor_contacto_id_9697d6c1_fk_shippers_gatewaycontactocondutor_id] FOREIGN KEY ([contacto_id]) REFERENCES [shippers_gatewaycontactocondutor] ([id]);
CREATE INDEX [shippers_gatewayprimeiramatricula_empresa_id_2a86ad73] ON [shippers_gatewayprimeiramatricula] ([empresa_id]);
CREATE INDEX [shippers_ptpriv_pt_part_2_id_88a53124] ON [shippers_ptpriv] ([pt_part_2_id]);
ALTER TABLE [shippers_gatewayinfocondutor] ADD CONSTRAINT [shippers_gatewayinfocondutor_condutorID_id_5ce55aa0_fk_shippers_gatewaycondutorid_id] FOREIGN KEY ([condutorID_id]) REFERENCES [shippers_gatewaycondutorid] ([id]);
ALTER TABLE [shippers_gatewayprimeiramatricula] ADD CONSTRAINT [shippers_gatewayprimeiramatricula_empresa_id_2a86ad73_fk_shippers_gatewayempresa_id] FOREIGN KEY ([empresa_id]) REFERENCES [shippers_gatewayempresa] ([id]);
ALTER TABLE [shippers_gatewayinfocondutor] ADD CONSTRAINT [shippers_gatewayinfocondutor_condutor_id_a3a03741_fk_shippers_gatewaycondutor_id] FOREIGN KEY ([condutor_id]) REFERENCES [shippers_gatewaycondutor] ([id]);
