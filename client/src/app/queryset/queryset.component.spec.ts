import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuerysetComponent } from './queryset.component';

describe('QuerysetComponent', () => {
  let component: QuerysetComponent;
  let fixture: ComponentFixture<QuerysetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuerysetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuerysetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
