import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { XioDialogComponent } from './xio-dialog.component';

describe('XioDialogComponent', () => {
  let component: XioDialogComponent;
  let fixture: ComponentFixture<XioDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ XioDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(XioDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
