import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { XioProgressComponent } from './xio-progress.component';

describe('XioProgressComponent', () => {
  let component: XioProgressComponent;
  let fixture: ComponentFixture<XioProgressComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ XioProgressComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(XioProgressComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
