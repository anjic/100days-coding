import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModifyButtonComponent } from './modify-button.component';

describe('ModifyButtonComponent', () => {
  let component: ModifyButtonComponent;
  let fixture: ComponentFixture<ModifyButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModifyButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModifyButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
