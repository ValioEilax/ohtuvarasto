import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #Tilavuus 0.0, kun negatiivinen "tilavuus" annetaan
    def test_tilavuus_negatiivinen(self):
        self.varasto = Varasto(-1.0)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)
        
    def test_alku_saldo_negatiivinen(self):
        self.varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0.0) 
        
    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0) 
        
    def test_lisaa_varastoon_yli_saldon(self):
        self.varasto = Varasto(10, 5)
        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus) 
        
    def test_ota_negatiivinen(self):
        tasku = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(tasku, 0) 
    
    def test_ota_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(10)
        tasku = self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(tasku, 10) 

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä ")