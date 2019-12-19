import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuerysetsComponent } from './querysets.component';

describe('QuerysetsComponent', () => {
  let component: QuerysetsComponent;
  let fixture: ComponentFixture<QuerysetsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuerysetsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuerysetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
