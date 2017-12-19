import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmailDeleteComponent } from './email-delete.component';

describe('EmailDeleteComponent', () => {
  let component: EmailDeleteComponent;
  let fixture: ComponentFixture<EmailDeleteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmailDeleteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmailDeleteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
