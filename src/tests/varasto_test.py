import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_negatiivinen_tilavuus(self):
        self.assertEquals(Varasto(-1).tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        self.assertEquals(Varasto(0, -1).saldo, 0)
    
    def test_negatiivinen_lisays(self):
        self.assertEquals(self.varasto.lisaa_varastoon(-1), None)

    def test_valmiiksi_taynna(self):
        self.assertEquals(Varasto(5, 10).saldo, 5)
    
    def test_liiallisen_lisays(self):
        self.varasto.lisaa_varastoon(500)
        self.assertEquals(self.varasto.saldo, self.varasto.tilavuus)

    def test_tulostus_oikea(self):
        self.assertEquals(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_liiallinen_ottaminen_varastosta(self):
        self.varasto.lisaa_varastoon(1)
        self.assertEquals(self.varasto.ota_varastosta(20), 100)
        self.assertEquals(self.varasto.saldo, 0.0)

    def test_ota_negatiivinen_varastosta(self):
        self.assertEquals(self.varasto.ota_varastosta(-50), 0.0)

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
