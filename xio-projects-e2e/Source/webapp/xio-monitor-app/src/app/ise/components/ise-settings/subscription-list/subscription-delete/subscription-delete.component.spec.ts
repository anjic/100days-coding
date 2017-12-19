import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SubscriptionDeleteComponent } from './subscription-delete.component';

describe('SubscriptionDeleteComponent', () => {
  let component: SubscriptionDeleteComponent;
  let fixture: ComponentFixture<SubscriptionDeleteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SubscriptionDeleteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SubscriptionDeleteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
