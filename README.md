# Flask exploration

## Day 1

- Creating flask app and set the app.run for the dev server.
- app.route decorator functionality.
- Passing variables to the context of the render_template method.
- Conditional HTML rendering with the Jinja2 template
- Custom Error Pages
- Tailwind integration with flask project

## Day 2

- Extend the flask template
- Generating a URL's to the given endpoint with the given values.
- Styling with Bootstrap 5

## Day 3

- Web Forms with WTF

```python
  class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
```

## Field types:

**BooleanField** <br>
**DateField** <br>
**DateTimeField** <br>
**DecimalField** <br>
**FileField** <br>
**HiddenField** <br>
**MultipleFileField** <br>
**FieldList** <br>
**FloatField** <br>
**FormField** <br>
**IntegerField** <br>
**PasswordField** <br>
**RadioField** <br>
**SelectField** <br>
**SelectMultipleField** <br>
**SubmitField** <br>
**StringField** <br>
**TextAreaField** <br>
**TimeField** <br>

## Validators:

**DataRequired** <br>
**Email** <br>
**EqualTo** <br>
**InputRequired** <br>
**IPAddress** <br>
**Length** <br>
**MacAddress** <br>
**NumberRange** <br>
**Optional** <br>
**Regexp** <br>
**URL** <br>
**UUID** <br>
**AnyOf** <br>
**NoneOf** <br>
