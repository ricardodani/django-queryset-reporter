export class Queryset {
  id: number;
  name: string;
  model: number;
  distinct: boolean;
  createdAt: Date;
  modifiedAt: Date;

  constructor(private _data: object) {
    this.id = _data['id'];
    this.name = _data['name'];
    this.model = _data['model'];
    this.distinct = _data['distinct'];
    this.createdAt = _data['created_at'];
    this.modifiedAt = _data['modified_at'];
  }

  getFormData() {
    return {
      name: this.name,
      model: this.model,
      distinct: this.distinct
    }
  }

}


export class Model {
  id: number;
  name: string;

  constructor(private _data: object) {
    this.id = _data['id'];
    this.name = _data['name'];
  }
}
