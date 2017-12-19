import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QueueDepthComponent } from './queue-depth.component';

describe('QueueDepthComponent', () => {
  let component: QueueDepthComponent;
  let fixture: ComponentFixture<QueueDepthComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QueueDepthComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QueueDepthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
