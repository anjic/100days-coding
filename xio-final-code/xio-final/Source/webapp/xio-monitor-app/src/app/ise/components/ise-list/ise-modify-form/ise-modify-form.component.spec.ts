import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseModifyFormComponent } from './ise-modify-form.component';

describe('IseModifyFormComponent', () => {
  let component: IseModifyFormComponent;
  let fixture: ComponentFixture<IseModifyFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseModifyFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseModifyFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
