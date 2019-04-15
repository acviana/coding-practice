require File.expand_path(File.dirname(__FILE__) + '/neo')

class AboutNil < Neo::Koan
  def test_nil_is_an_object
    assert_equal true, nil.is_a?(Object), "Unlike NULL in other languages"
  end

  def test_you_dont_get_null_pointer_errors_when_calling_methods_on_nil
    # What happens when you call a method that doesn't exist.  The
    # following begin/rescue/end code block captures the exception and
    # makes some assertions about it.
    begin
      nil.some_method_nil_doesnt_know_about
    rescue Exception => ex
      # What exception has been caught?
      assert_equal NoMethodError, ex.class

      # What message was attached to the exception?
      # (HINT: replace __ with part of the error message.)
      assert_match(/undefined method `some_method_nil_doesnt_know_about' for nil:NilClass/, ex.message)
    end
  end

  def test_nil_has_a_few_methods_defined_on_it
    assert_equal true, nil.nil?
    assert_equal "", nil.to_s
    assert_equal "nil", nil.inspect

    # THINK ABOUT IT:
    #
    # Is it better to use
    #    obj.nil?
    # or
    #    obj == nil
    # Why?
    #
    # Dharma: They are the same up to a "micro optimization" or some
    # crazy overloading.
    #
    # This is slighlty different from Python where None is a singleton
    # and the preference is to use "is None" over "== None" to
    # differentiate between an object that evaluates to None vs the
    # actual None object itself. Arguably, this is also a micro
    # optimization around a crazy overloading corner case.
    #
    # Sources:
    # - https://stackoverflow.com/a/1972305/1216837
    # - https://stackoverflow.com/a/3257951/1216837
  end

end
