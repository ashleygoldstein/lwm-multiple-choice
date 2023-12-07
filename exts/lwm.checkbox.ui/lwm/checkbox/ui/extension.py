import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[lwm.checkbox.ui] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class LwmCheckboxUiExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[lwm.checkbox.ui] lwm checkbox ui startup")


        self._window = ui.Window("Multiple Choice UI", width=600, height=100)
        with self._window.frame:
            with ui.VStack(height=40):
                    with ui.HStack(height=10, width=10):
                        ui.Spacer(width=4)
                        ui.Label("Shopping List:")
                        
                        ui.Spacer(width=4)
                        first = ui.CheckBox(name="Apples")
                        ui.Spacer(width=4)
                        first_stringfield = ui.Label("Apples", width=80, height=20)

                        ui.Spacer(width=4)
                        second = ui.CheckBox()
                        ui.Spacer(width=4)
                        second_stringfield = ui.Label("Oranges", width=80, height=20)

                        ui.Spacer(width=4)
                        third = ui.CheckBox()
                        ui.Spacer(width=4)
                        third_stringfield = ui.Label("Bananas", width=80, height=20)



                    def like_radio(model, first, second):
                        '''Turn on the model and turn off two checkboxes'''
                        if model.get_value_as_bool():
                            model.set_value(True)
                            first.model.set_value(False)
                            second.model.set_value(False)


                    # Connect one to another
                    first.model.add_value_changed_fn(
                        lambda a, b=second, c=third: like_radio(a, b, c))
                    second.model.add_value_changed_fn(
                        lambda a, b=first, c=third: like_radio(a, b, c))
                    third.model.add_value_changed_fn(
                        lambda a, b=first, c=second: like_radio(a, b, c))

    def on_shutdown(self):
        print("[lwm.checkbox.ui] lwm checkbox ui shutdown")
