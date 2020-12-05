import unittest
import re


passport_rules = {
    'byr': lambda v: int(v)>=1920 and int(v)<=2002, 
    'iyr': lambda v: int(v)>=2010 and int(v)<=2020,
    'eyr': lambda v: int(v)>=2020 and int(v)<=2030,
    'hgt': lambda v: re.compile('^(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)$').match(v),
    'hcl': lambda v: re.compile('^#[a-f0-9]{6}$').match(v),
    'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda v: re.compile('^[0-9]{9}$').match(v)
    }

class TestPassportRules(unittest.TestCase):
    def test_pid(self):
        vf = passport_rules['pid']
        self.assertTrue(vf('012345678'))
        self.assertFalse((vf('0123456789')))
        self.assertFalse((vf('1234567890')))
        self.assertFalse((vf('123456789a')))
        
    def test_byr(self):
        vf = passport_rules['byr']
        self.assertTrue(vf('1920'))
        self.assertTrue(vf('2002'))
        self.assertTrue(vf('1954'))
        self.assertFalse(vf('1900'))
        self.assertFalse(vf('2021'))

    def test_hgt(self):
        vf = passport_rules['hgt']
        self.assertTrue(vf('150cm'))
        self.assertTrue(vf('193cm'))
        self.assertTrue(vf('161cm'))
        self.assertTrue(vf('170cm'))
        self.assertTrue(vf('59in'))
        self.assertTrue(vf('59in'))
        self.assertTrue(vf('76in'))
        self.assertTrue(vf('68in'))
        self.assertTrue(vf('75in'))
        self.assertFalse(vf('150in'))
        self.assertFalse(vf('150in150in150in'))
        self.assertFalse(vf('40in'))
        self.assertFalse(vf('58in'))
        self.assertFalse(vf('77in'))
        self.assertFalse(vf('194cm'))
        self.assertFalse(vf('7777'))
        self.assertFalse(vf('dsfsdfd'))

    def test_hcl(self):
        vf = passport_rules['hcl']
        self.assertTrue(vf('#666666'))
        self.assertTrue(vf('#6fd666'))
        self.assertTrue(vf('#666666'))
        self.assertTrue(vf('#aaaaaa'))
        self.assertTrue(vf('#63420c'))
        self.assertFalse(vf('#66sdf6'))
        self.assertFalse(vf('666666'))
        self.assertFalse(vf('r889890'))
        self.assertFalse(vf('#!66666'))
        self.assertFalse(vf('fqefqewefewfewf'))
        self.assertFalse(vf('aaaa#6fd666'))
        self.assertFalse(vf('#6fd666#6fd666'))

if __name__ == '__main__':
    unittest.main()
