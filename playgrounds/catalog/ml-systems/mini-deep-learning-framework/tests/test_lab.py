import unittest
from lab import Model
class ModelTest(unittest.TestCase):
    def test_step(self):
        m=Model({'w':1.0}); m.step({'w':0.5}, lr=0.1); self.assertAlmostEqual(m.params['w'],0.95)
    def test_checkpoint(self):
        m=Model({'w':1.0}); ck=m.checkpoint(7); m2,step=Model.load(ck); self.assertEqual((m2.params,step), ({'w':1.0},7))
if __name__ == '__main__': unittest.main()
