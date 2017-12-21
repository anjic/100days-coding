import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { XioLoaderComponent } from './xio-loader.component';

describe('XioLoaderComponent', () => {
  let component: XioLoaderComponent;
  let fixture: ComponentFixture<XioLoaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ XioLoaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(XioLoaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
