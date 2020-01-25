export class Field {
  public fieldName: string;
  public fieldVerbose: string;
  public fieldType: string;

  constructor(private fieldJson: object) {
    this.fieldName = fieldJson['field'];
    this.fieldVerbose = fieldJson['field_verbose'];
    this.fieldType = fieldJson['field_type'];
  }
}

export class Result {

  public data: object;

  constructor(
    private resultJson: object,
    private fields: Field[]
  ) {
    fields.map(
      (field: Field) => {
        this.data[field.fieldName] = this.parseResult(resultJson, field);
      }
    )
  }

  private parseResult(resultJson: object, field: Field) {
    let value: any = resultJson[field.fieldName];
    /*switch (field.fieldType) {
      case 'DateTimeField':
        return new Date(value);
      case 'IntegerField':
        return parseInt(value);
      case 'FloatField': return parseFloat(value);
      default: return value;
    }*/
    return value;
  }

 }

export class QuerysetResult {

  public fields: Field[];
  public results: Result[];

  constructor(private resultJson) {
    this.fields = resultJson['fields'].map(
      (fieldJson: object) => new Field(fieldJson)
    );
    this.results.map(
      (resultJson: object) => new Result(resultJson, this.fields)
    )
  }

}
