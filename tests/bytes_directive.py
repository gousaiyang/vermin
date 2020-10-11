from .testutils import VerminTest, current_version

class VerminBytesDirectiveTests(VerminTest):
  def test_b_directive(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 5), self.detect("b'%b'"))

  def test_a_directive(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 5), self.detect("b'%a'"))

  def test_r_directive(self):
    if current_version() >= 3.0:
      self.assertOnlyIn(((2, 7), (3, 5)), self.detect("b'%r'"))
